fn main() {
    let my_vec: Vec<i32> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("{:?}", binary_search(&my_vec, 10));
}

// return enum with 2 options: Ok(usize) and Err(&'static str) = string slice with static lifetime ("for the entire duration of the program")
fn binary_search(arr: &[i32], item: usize) -> Result<usize, &'static str> {
    if arr.is_empty() {
        return Err("array is empty")
    }
    let mut low: usize = 0;
    let mut high: usize = arr.len() - 1;

    // binary search implementation
    while low <= high {
        // mid calculation prevents overflow (just low + high = big number together, below first we decrease number then add)
        let mid: usize = low + (high - low) / 2;
        let guess: usize = arr[mid] as usize;

        if guess == item {
            return Ok(mid);
        } else if guess > item {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    Err("Your item not found")
}

