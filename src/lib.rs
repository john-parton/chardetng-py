use chardetng::EncodingDetector;
use pyo3::prelude::*;

/// detect(byte_str, /)
/// --
///
/// Detect the encoding of byte_str and return the encoding.
///
///     Parameters
///     ----------
///     byte_str : bytes or bytearray
///         Input buffer to decode.
///
///     Returns
///     -------
///     str
///         The decoded string.
#[pyfunction]
fn detect(buffer: Vec<u8>) -> &'static str {
    let mut detector = EncodingDetector::new();

    detector.feed(&buffer, true);

    detector.guess(None, true).name()
}

#[pymodule]
fn _rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(detect, m)?)?;
    Ok(())
}
