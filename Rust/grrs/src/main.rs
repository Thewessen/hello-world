extern crate clap_verbosity_flag;

use structopt::StructOpt;
use log::{info, error};
use std::io::{self, BufRead, BufReader, BufWriter, Write};
use std::process::exit;
use std::fs::File;

#[derive(StructOpt, Debug)]
struct Cli {
    pattern: String,
    #[structopt(parse(from_os_str))]
    path: std::path::PathBuf,
    #[structopt(flatten)]
    verbose: clap_verbosity_flag::Verbosity,
}

fn main() {
    env_logger::init();
    info!("Reading cli args...");
    let args = Cli::from_args();

    // optimizing buffer for reading files
    info!("Reading from {:?}", &args.path);
    let file = File::open(&args.path);
    if let Err(err) = file {
        error!("Could not read from {:?}: {}", &args.path, err);
        exit(1)
    }

    info!("Creating a buffer for reading...");
    let reader = BufReader::new(file.unwrap());

    // optimizing buffer for writing
    info!("Creating a buffer for writing to stdout...");
    let stdout = io::stdout();
    let mut writer = BufWriter::new(stdout);

    info!("Iterating over all lines in file");
    for (i, poss_line) in reader.lines().enumerate() {
        info!("Processing line {}...", i);
        match poss_line {
            Ok(line) => {
                if line.contains(&args.pattern) {
                    info!("'{}' found on line {}...", &args.pattern, i);
                    if let Err(err) = writeln!(writer, "{}: {}", i, line) {
                        error!("Unable to write line {:?}:{} to stdout: {}", &args.path, i, err)
                    }
                }
            },
            Err(err) => error!("Unable to read line {:?}:{}: {}", &args.path, i, err)
        };
    };
}
