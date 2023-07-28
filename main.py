def calculate_match_rate(file_path, log_file_path, output_file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()

    total_words = len(words)
    matches = 0
    matched_words = []

    with open(log_file_path, 'r') as log_file:
        log_lines = log_file.readlines()

    for line in log_lines:
        line_words = line.split()
        matches_in_line = [word for word in words if word in line_words]
        if matches_in_line:
            matches += len(matches_in_line)
            matched_words.extend(matches_in_line)

    match_rate = matches / total_words * 100

    with open(output_file_path, 'w') as matched_file:
        for word in matched_words:
            matched_file.write(word + '\n')

    return match_rate, matches



# ファイルパス
password_file_path = 'password_list/password_dir/password'
extra_lower_file_path = 'password_list/extra/lower'
password_lower_file_path = 'password_list/password_dir/lower'
japanese_lower_file_path = 'password_list/japanese/lower'
japanese_mixed_file_path = 'password_list/japanese/mixed'
# japanese_mixed_file_path = 'password_list/SecLists/Passwords/xato-net-10-million-passwords.txt'

log_file_path = 'convert_log/converted_password.log'

# ファイル行数を取得
def get_file_line_count(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)

# ファイル行数を取得
password_line_count = get_file_line_count(password_file_path)
samall_lower_line_count = get_file_line_count(password_lower_file_path)
extra_lower_line_count = get_file_line_count(extra_lower_file_path)
japanese_lower_line_count = get_file_line_count(japanese_lower_file_path)
japanese_mixed_line_count = get_file_line_count(japanese_mixed_file_path)

# 書き込みファイルパス
output_file_matched_password = 'matched_output/matched_words_password.txt'
output_file_matched_small_lower = 'matched_output/matched_words_small_lower.txt'
output_file_matched_extra_lower = 'matched_output/matched_words_extra_lower.txt'
output_file_matched_japanese_lower = 'matched_output/matched_words_japanese_lower.txt'
output_file_matched_japanese_mixed = 'matched_output/matched_words_japanese_mixed.txt'

# Password Match Rate
matched_password_match_rate, matched_password_matches = calculate_match_rate(password_file_path, log_file_path, output_file_matched_password)

# Small Lower Match Rate
matched_small_lower_match_rate, matched_small_lower_matches = calculate_match_rate(password_lower_file_path, log_file_path, output_file_matched_small_lower)

# Extra Lower Match Rate

matched_extra_lower_match_rate, matched_extra_lower_matches = calculate_match_rate(extra_lower_file_path, log_file_path, output_file_matched_extra_lower)

# Japanese Lower Match Rate
matched_japanese_lower_match_rate, matched_japanese_lower_matches = calculate_match_rate(japanese_lower_file_path, log_file_path, output_file_matched_japanese_lower)

# Japanese Mixed Match Rate
matched_japanese_mixed_match_rate, matched_japanese_mixed_matches = calculate_match_rate(japanese_mixed_file_path, log_file_path, output_file_matched_japanese_mixed)


# Print results
print("------------------------------------")
print("Password File Line Count:", password_line_count)
print(f"Password Match Rate: {matched_password_match_rate:.2f}%")
print(f"Password Matches: {matched_password_matches}/{password_line_count}")
print("------------------------------------")
print("Password Lower File Line Count:", samall_lower_line_count)
print(f"Password Lower Match Rate: {matched_small_lower_match_rate:.2f}%")
print(f"Password Lower Matches: {matched_small_lower_matches}/{samall_lower_line_count}")
print("------------------------------------")
print("Extra Lower File Line Count:", extra_lower_line_count)
print(f"Extra Lower Match Rate: {matched_extra_lower_match_rate:.2f}%")
print(f"Extra Lower Matches: {matched_extra_lower_matches}/{extra_lower_line_count}")
print("------------------------------------")
print("Japanese Lower File Line Count:", japanese_lower_line_count)
print(f"Japanese Lower Match Rate: {matched_japanese_lower_match_rate:.2f}%")
print(f"Japanese Lower Matches: {matched_japanese_lower_matches}/{japanese_lower_line_count}")
print("------------------------------------")
print("Japanese Mixed File Line Count:", japanese_mixed_line_count)
print(f"Japanese Mixed Match Rate: {matched_japanese_mixed_match_rate:.2f}%")
print(f"Japanese Mixed Matches: {matched_japanese_mixed_matches}/{japanese_mixed_line_count}")
print("------------------------------------")

