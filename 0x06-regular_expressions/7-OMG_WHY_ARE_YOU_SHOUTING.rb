#!/usr/bin/env ruby
#A regular expression that must be only matching CAPITAL LETTERS
puts ARGV[0].scan(/[A-Z]/).join
