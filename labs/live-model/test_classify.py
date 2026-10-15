"""Adapter contract tests; no Ollama installation or network needed."""
import io
import json
import unittest
from http.client import IncompleteRead
from urllib.error import URLError

from classify import classify


def response_for(content, **fields):
    envelope = {"done": True, "model": "test-model",
                "message": {"content": json.dumps(content)}, **fields}
    return io.BytesIO(json.dumps(envelope).encode())


class AdapterTests(unittest.TestCase):
    def test_request_contract_and_valid_prediction(self):
        def transport(request, timeout):
            self.assertEqual(request.full_url, "http://127.0.0.1:11434/api/chat")
            payload = json.loads(request.data)
            self.assertFalse(payload["stream"])
            self.assertEqual(payload["model"], "test-model")
            self.assertNotIn("expected_label", payload)
            self.assertEqual(timeout, 60)
            return response_for({"label": "authentication", "evidence": "Sign-in fails."})
        result = classify("Sign-in fails.", "test-model", transport=transport)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["prediction"]["label"], "authentication")
        self.assertIn("raw_response", result)

    def test_connection_failure_is_not_a_valid_prediction(self):
        for error in (URLError("simulated connection failure"), IncompleteRead(b"partial")):
            with self.subTest(error=type(error).__name__):
                def transport(request, timeout):
                    raise error
                result = classify("A bug.", "test-model", transport=transport)
                self.assertEqual(result["status"], "application_error")
                self.assertNotIn("prediction", result)

    def test_timeout_is_recorded(self):
        def transport(request, timeout):
            raise TimeoutError("simulated timeout")
        self.assertEqual(classify("A bug.", "test-model", transport=transport)["status"],
                         "application_error")

    def test_invalid_model_json_is_not_a_valid_prediction(self):
        for raw in (b'{"done":true,"message":{"content":"not-json"}}', b'\xff'):
            with self.subTest(raw=raw):
                def transport(request, timeout):
                    return io.BytesIO(raw)
                self.assertEqual(classify("A bug.", "test-model", transport=transport)["status"],
                                 "invalid_output")

    def test_invalid_shapes_and_labels_are_rejected(self):
        for content in ([], {"label": [], "evidence": "text"},
                        {"label": "invented", "evidence": "text"},
                        {"label": "other", "evidence": ""}):
            with self.subTest(content=content):
                def transport(request, timeout):
                    return response_for(content)
                result = classify("A bug.", "test-model", transport=transport)
                self.assertEqual(result["status"], "invalid_output")

    def test_incomplete_response_is_rejected(self):
        def transport(request, timeout):
            return response_for({"label": "other", "evidence": "Unclear."}, done=False)
        self.assertEqual(classify("A bug.", "test-model", transport=transport)["status"],
                         "invalid_output")

    def test_invalid_input_never_reaches_transport(self):
        def transport(request, timeout):
            self.fail("Invalid input must not make a request")
        for timeout in (0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                classify("A bug.", "test-model", timeout, transport)
        with self.assertRaises(ValueError):
            classify(" ", "test-model", transport=transport)


if __name__ == "__main__":
    unittest.main()
