use wasm_bindgen::prelude::*;
use rand::Rng;

/*
// When the `wee_alloc` feature is enabled, use `wee_alloc` as the global
// allocator.
#[cfg(feature = "wee_alloc")]
#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;
*/

#[wasm_bindgen]
extern {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn greet() {
    alert("Hello, mathgenerator!");
}

#[wasm_bindgen]
/// Adds two numbers
pub fn addition(max_term : u8) -> Vec<String> {
    let mut rng = rand::thread_rng();
    let a : u8 = rng.gen_range(0..max_term);
    let b : u8 = rng.gen_range(0..max_term);
    let prob : String = format!("${} + {} =$", a, b);
    let sol : String = format!("${}$", a + b);
    return vec![prob, sol];
}

