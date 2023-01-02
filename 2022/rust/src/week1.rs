use std::fs;

pub fn day1() {
    println!("Day 1: ");
    let contents = fs::read_to_string("./src/input/day1.txt").expect("Should have been able to read the file");
    let mut first = 0;
    let mut second = 0;
    let mut third = 0;
    let mut this_elf  = 0;
    for row in contents.split("\n") {
        if row != "" {
            this_elf += row.parse::<i32>().unwrap();
        } else {
            if this_elf > first {
                third = second;
                second = first;
                first = this_elf;
            } else if this_elf > second {
                third = second;
                second = this_elf;
            } else if this_elf > third {
                third = this_elf;
            }
            this_elf = 0;
        } 
    }
    if this_elf > first {
        third = second;
        second = first;
        first = this_elf;
    } else if this_elf > second {
        third = second;
        second = this_elf;
    } else if this_elf > third {
        third = this_elf;
    }
    println!("First: {}", first);
    println!("Total: {}", first+second+third);
}

pub fn day2()
{
    println!("\nDay 2: ");
    let contents = fs::read_to_string("./src/input/day2.txt")
        .expect("Should have been able to read the file");
    let mut my_point = 0;
    for row in contents.split("\n") {
        let vec: Vec<&str> = row.split(" ").collect();
        match vec[0] {
            "A" => { // Rock
                match vec[1] {
                    "X" => my_point += 3 + 0,
                    "Y" => my_point += 1 + 3,
                    "Z" => my_point += 2 + 6,
                    &_ => (),
                }
            }
            "B" => { // Paper
                match vec[1] {
                    "X" => my_point += 1 + 0,
                    "Y" => my_point += 2 + 3,
                    "Z" => my_point += 3 + 6,
                    &_ => (),
                }
            }
            "C" => { //scissor
                match vec[1] {
                    "X" => my_point += 2 + 0,
                    "Y" => my_point += 3 + 3,
                    "Z" => my_point += 1 + 6,
                    &_ => (),
                }
            }
            &_ => (),
        }
    } 
    println!("my_point: {}", my_point);
}


pub fn day3()
{
    println!("\nDay 3: ");
    let contents = fs::read_to_string("./src/input/day3.txt")
        .expect("Should have been able to read the file");
    let mut j = Vec::new();//first[0];
    for row in contents.split("\n") {
        let vec: Vec<&str> = row.split("").collect();
        let length = vec.len();
        println!("{length}");
        let mut first = Vec::new();
        let mut second = Vec::new();
        for (i, letter) in vec.iter().enumerate() {
            if i < length/2 {
                first.push(letter);
            } else {
                second.push(letter);
            }
        }
        
        for l in first {
            println!("{l}");
            if second.iter().any(|&i| i==l) {
                j.push(l);
                println!("{l}");
                println!("l");
                //break;
            }
            
        }
        for k in j{
            println!("{k}");
        }
        
    }
}