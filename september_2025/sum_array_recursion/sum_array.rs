fn sum_array(vector: &Vec<i64>) -> i64 {
    if vector.len() == 0 {
        return 0
    }
    // On every recursive call, allocates a new Vec<i64> for vector[1..]. (inefficient)
    return vector[0] + sum_array(&vector[1..].to_vec());
}


fn main() {
    let x: Vec<i64> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("{}", sum_array(&x));
}