import unittest
from backend.src.ingestion.document_ai import extract_text_from_pdf
from backend.src.ingestion.ocr_utils import perform_ocr
from backend.src.ingestion.summarizer import summarize_text

class TestIngestion(unittest.TestCase):

    def test_extract_text_from_pdf(self):
        # Test case for extracting text from a sample PDF
        pdf_path = 'tests/sample.pdf'  # Path to a sample PDF for testing
        extracted_text = extract_text_from_pdf(pdf_path)
        self.assertIsInstance(extracted_text, str)
        self.assertGreater(len(extracted_text), 0)

    def test_perform_ocr(self):
        # Test case for performing OCR on a sample image
        image_path = 'tests/sample_image.png'  # Path to a sample image for testing
        ocr_text = perform_ocr(image_path)
        self.assertIsInstance(ocr_text, str)
        self.assertGreater(len(ocr_text), 0)

    def test_summarize_text(self):
        # Test case for summarizing extracted text
        sample_text = "This is a test document containing multiple sentences."
        summary = summarize_text(sample_text)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

if __name__ == '__main__':
    unittest.main()