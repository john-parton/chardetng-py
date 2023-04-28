use chardetng::EncodingDetector;
use pyo3::prelude::*;

use std::str;

use encoding_rs::UTF_8;
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

#[pyfunction]
fn decode(buffer: Vec<u8>) -> String {
    let mut detector = EncodingDetector::new();

    detector.feed(&buffer, true);

    // Python does not do bom_handling by default
    // this matches the python output , maybe?
    let (cow, _had_errors) = detector.guess(None, true).decode_without_bom_handling(&buffer);

    cow.to_string()
}

// #[pyfunction]
// fn test_string() -> (String, bool) {
//     let zero_width_no_break_space = vec![0xef, 0xbb, 0xbf];
//     // str::from_utf8(&zero_width_no_break_space).unwrap().to_string()

//     let (cow, had_errors) = UTF_8.decode_without_bom_handling(&zero_width_no_break_space);

//     (cow.to_string(), had_errors)
// }


#[pymodule]
fn _rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(detect, m)?)?;
    m.add_function(wrap_pyfunction!(decode, m)?)?;
    // m.add_function(wrap_pyfunction!(test_string, m)?)?;
    Ok(())
}
