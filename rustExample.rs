fn main() {
   
    let numbers = [10, 20, 30, 40, 50];

 
    println!("Printing elements of the array:");
    for &num in numbers.iter() {
       
         println!("{}", num);
    }


    let mut sum = 0;
    for &num in numbers.iter() {
        
            sum += num;
    }
    println!("Sum of all elements: {}", sum);

    let mut max = numbers[0];
    for &num in numbers.iter() {
        if num > max {
                 max = num;
        }
    }
    println!("Maximum element in the array: {}", max);

    
    let mut doubled_numbers = [0; 5]; 
    for (i, &num) in numbers.iter().enumerate() {
             doubled_numbers[i] = num * 2;
    }
    println!("Doubled array: {:?}", doubled_numbers);
}

