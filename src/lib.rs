use pyo3::prelude::*;
use chardetng::EncodingDetector;


#[pyfunction]
fn decode(buffer: &[u8]) -> String {
    let mut detector = EncodingDetector::new();

    detector.feed(buffer, true);

    let (cow, _encoding_used, _had_errors) =  detector.guess(None, true).decode(&buffer);

    cow.to_string()
}


/// A Python module implemented in Rust.
#[pymodule]
fn chardetng_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(decode, m)?)?;
    Ok(())
}