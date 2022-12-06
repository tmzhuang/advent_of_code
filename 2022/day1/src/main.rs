use std::fs;

const N: usize = 3;

fn part1() {
    let file_path = "/media/downloads/input.txt";
    let data = fs::read_to_string(file_path)
        .expect("Cannot read file at {file_path}.");

    let lines = data.split("\n");
    let mut acc: u64 = 0;
    let mut max: u64 = 0;
    for line in lines {
        if line.trim().is_empty() {
            if acc > max {
                max = acc;
            }
            acc = 0;
        } else {
            let value: u64 = line.parse().expect("Not a number.");
            acc += value;
        }
    }
    println!("max: {max}");
}

fn part2() {
    let file_path = "/media/downloads/input.txt";
    let data = fs::read_to_string(file_path)
        .expect("Cannot read file at {file_path}.");
    let mut top = [0; N];
    let lines = data.split("\n");
    let mut acc: u64 = 0;
    for line in lines {
        if line.trim().is_empty() {
            // assume top is already sorted
            // top[0] is the smallest number
            if acc > top[0] {
                top[0] = acc;
                top.sort();
            }
            acc = 0;
        } else {
            let value: u64 = line.parse().expect("Not a number.");
            acc += value;
        }
    }
    let sum: u64 = top.iter().sum();
    println!("Total calories of top 3 elves: {sum}");
}

fn main() {
    part1();
    part2();
}
