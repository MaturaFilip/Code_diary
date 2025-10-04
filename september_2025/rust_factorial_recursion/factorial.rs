fn main() {
    let arr: Vec<i64> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("{:?}", factorio(&arr));
}

fn factorio(arr: &[i64]) -> i64 {
    if arr.is_empty() {
        1
    } else {
        arr[0] * factorio(&arr[1..])
    }
}