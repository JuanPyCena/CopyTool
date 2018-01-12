#!/usr/bin/env bash
xcode-select --install
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
brew install python3
pip3 install guizero
pip3 install datetime