
/*Determine exact spot in which it will break in the most optimized way */


fn main() {
    let mut arr = vec![false; 101];
    for i in 67..101 {
        arr[i] = true;
    }

    let index_when_break = crystal_problem(&arr);
    println!("{:?}", index_when_break.unwrap());

}

fn crystal_problem(arr: &[bool]) -> Result<usize, &str> {
    // square_root(len(arr))
    // prevent step_by 0 with .max(1)
    let sq_number = arr.len().isqrt().max(1);
    // iterate with square root steps, until you find true
    for i in (0..arr.len()).step_by(sq_number) {
        if arr[i] == true {
            // go back to previous square root position, iterate by one, if you find true -> return position
            for j in (i-sq_number)..arr.len() {
                if arr[j] == true {
                    return Ok(j);
                }
            }
        }
    }
    return Err("No true value found");

}

