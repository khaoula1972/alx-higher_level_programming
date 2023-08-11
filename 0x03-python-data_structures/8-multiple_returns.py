#!/usr/bin/python3
def multiple_returns(sentence):
    char = sentence[0] if len(sentence) >= 1 else None
    return (len(sentence), char)
