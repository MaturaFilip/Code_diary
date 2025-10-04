fn selection_sort(arr: &mut [i64]) {
    // saturating_sub = subtraction that never underflows
    // If the result would be negative, it "saturates" at zero instead.
    for i in 0..arr.len().saturating_sub(1) {
        let mut smallest_idx = i;
        for j in (i+1)..arr.len() {
            if arr[j] < arr[smallest_idx] {
                smallest_idx = j
            }
        }
        arr.swap(i, smallest_idx);
    }
}


fn main() {
    let mut unsorted_arr: Vec<i64> = vec![10, 8, 5, 12, 0, 3, 5];

    selection_sort(&mut unsorted_arr);
    println!("{:?}", unsorted_arr);
}

