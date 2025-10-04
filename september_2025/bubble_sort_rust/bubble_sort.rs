fn bubble_sort(arr: &mut Vec<i64>) -> &mut Vec<i64> {
    let mut length = arr.len();
    //let mut swapping: bool = true;

    while length > 0 {
        //swapping = false;
        for number in 1..length {
            if arr[number-1] > arr[number] {
                arr.swap(number-1, number);
                //swapping = true;
            }
        }
        length -= 1;
    }
    return arr;
}


fn main() {
    let mut unsorted_array: Vec<i64> = vec![7, 3, 0, 9, 10, 1];

    println!("{:?}", bubble_sort(&mut unsorted_array));
    println!("{:?}", unsorted_array);
}