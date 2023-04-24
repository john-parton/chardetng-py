use pyo3::prelude::*;
use pyo3::types::PyBytes;
use chardetng::EncodingDetector;


#[pyfunction]
fn decode(buffer: &PyBytes) -> (String, &str, bool) {
    let mut detector = EncodingDetector::new();

    let buffer_bytes = buffer.as_bytes();

    detector.feed(buffer_bytes, true);

    let (cow, encoding_used, had_errors) =  detector.guess(None, true).decode(&buffer_bytes);

    (cow.to_string(), encoding_used.name(), had_errors)
}


/// A Python module implemented in Rust.
#[pymodule]
fn chardetng_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(decode, m)?)?;
    Ok(())
}