use chardetng::EncodingDetector;
use pyo3::prelude::*;


#[doc = include_str!("../chardetng_docs/EncodingDetector.md")]
#[pyclass(name="EncodingDetector")]
struct EncodingDetectorWrapper {
    encoding_detector: EncodingDetector,
}

#[pymethods]
impl EncodingDetectorWrapper {
    #[new]
    fn new() -> Self {
        EncodingDetectorWrapper {
            encoding_detector: EncodingDetector::new()
        }
    }

    #[doc = include_str!("../chardetng_docs/feed.md")]
    #[pyo3(signature=(buffer, /, *, last))]
    fn feed(&mut self, buffer: Vec<u8>, last: bool) -> bool {
        self.encoding_detector.feed(&buffer, last)
    }

    #[doc = include_str!("../chardetng_docs/guess.md")]
    #[pyo3(signature=(*, tld, allow_utf8))]
    fn guess(&self, tld: Option<&[u8]>, allow_utf8: bool) -> &'static str {

        self.encoding_detector.guess(tld, allow_utf8).name()
    }

    #[doc = include_str!("../chardetng_docs/guess_assess.md")]
    #[pyo3(signature=(*, tld, allow_utf8))]
    fn guess_assess(&self, tld: Option<&[u8]>, allow_utf8: bool) -> (&'static str, bool) {

        let (encoding, higher_score) = self.encoding_detector.guess_assess(tld, allow_utf8);

        (
            encoding.name(),
            higher_score
        )
    }
}


#[pymodule]
fn detector(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<EncodingDetectorWrapper>()?;
    Ok(())
}
