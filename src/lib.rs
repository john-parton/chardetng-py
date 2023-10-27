use chardetng::EncodingDetector;
use pyo3::prelude::*;

// See https://github.com/john-parton/chardetng-py/issues/11
// Python prefers to use "cpXXX" for legacy encodings, while :code:`encoding_rs`
// and :code:`chardetng` use whatwg names.

// References
// ----------
// https://docs.python.org/3/library/codecs.html#standard-encodings
// https://encoding.spec.whatwg.org/#legacy-single-byte-encodings
fn _fix_encoding_name(encoding: &str) -> &str {
    match encoding.to_lowercase().as_str() {
        "windows-874" => "cp874",
        "gbk" => "gb18030",
        _ => encoding
    }
}

#[doc = include_str!("../chardetng_docs/EncodingDetector.md")]
#[pyclass(name = "EncodingDetector")]
struct EncodingDetectorWrapper {
    encoding_detector: EncodingDetector,
}

#[pymethods]
impl EncodingDetectorWrapper {
    #[new]
    fn new() -> Self {
        EncodingDetectorWrapper {
            encoding_detector: EncodingDetector::new(),
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
        _fix_encoding_name(self.encoding_detector.guess(tld, allow_utf8).name())
    }

    #[doc = include_str!("../chardetng_docs/guess_assess.md")]
    #[pyo3(signature=(*, tld, allow_utf8))]
    fn guess_assess(&self, tld: Option<&[u8]>, allow_utf8: bool) -> (&'static str, bool) {
        let (encoding, higher_score) = self.encoding_detector.guess_assess(tld, allow_utf8);

        (_fix_encoding_name(encoding.name()), higher_score)
    }
}

#[pymodule]
fn detector(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<EncodingDetectorWrapper>()?;
    Ok(())
}
