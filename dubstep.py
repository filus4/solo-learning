def song_decoder(song):
    pre_result = [word for word in song.split('WUB') if not word == '']
    result = ''.join(letters + ' ' for letters in pre_result)
    return result.strip()

def song_decoder_2(song):
    return " ".join(song.replace('WUB', ' ').split())


print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))