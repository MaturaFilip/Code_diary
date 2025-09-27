fn sum_array(slice: &[i64]) -> i64 {
    // with slices no allocation or ownership issues
    if slice.is_empty() {
        0
    } else {
        slice[0] + sum_array(&slice[1..])
    }
}


fn main() {
    let x = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("{:?}", sum_array(&x));
}

