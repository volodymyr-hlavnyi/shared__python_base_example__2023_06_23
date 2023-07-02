test_str = 'Hi test string for try some function of str python. Are you ok? '

print(f'.title() {test_str.title()}')
print(f'.upper() {test_str.upper()}')
print(f'.capitalized() {test_str.capitalize()}')
print(f'.casefold() {test_str.casefold()}')
print('.center(len(test_str)+10,-) {0}'.format(test_str.center(len(test_str)+10,'-')))

