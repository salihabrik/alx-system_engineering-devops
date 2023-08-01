#!/usr/bin/env ruby

# Function to extract sender, receiver, and flags information from the log
def extract_textme_info(log)
    sender = log.match(/\[from:(.*?)\]/)[1]
    receiver = log.match(/\[to:(.*?)\]/)[1]
    flags = log.scan(/\[flags:(.*?)\]/).join
    "#{sender},#{receiver},#{flags}"
  end
  
  # Check if the script is given a log file as an argument
  if ARGV.empty?
    puts "Usage: #{$PROGRAM_NAME} [log_file]"
    exit 1
  end
  
  log_file = ARGV[0]
  
  # Check if the log file exists
  unless File.file?(log_file)
    puts "Error: #{log_file} not found!"
    exit 1
  end
  
  log_lines = File.readlines(log_file)
  log_lines.each do |line|
    # Check if the line contains relevant information for text message transactions
    if line.include?('SMS [from:') && line.include?('[to:') && line.include?('[flags:')
      puts extract_textme_info(line)
    end
  end
  