use wasm_bindgen::prelude::*;
use rand::Rng;

#[wasm_bindgen]
/// Adds two numbers
pub fn addition(max_term : u8) -> js_sys::Array {
    let mut rng = rand::thread_rng();
    let a : u8 = rng.gen_range(0..max_term);
    let b : u8 = rng.gen_range(0..max_term);
    let prob : String = format!("${} + {} =$", a, b);
    let sum : u8 = a + b;
    let sol : String = format!("${}$", sum);
    [prob, sol]
}
