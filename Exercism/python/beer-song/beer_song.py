def recite(start: int, take: int = 1) -> list:
    """List the famous beer song"""
    song = list()
    for i in range(start, start-take, -1):
        if i == 0:
            song.append("No more bottles of beer on the wall, "
                        "no more bottles of beer.")
            song.append("Go to the store and buy some more, "
                        "99 bottles of beer on the wall.")
            break

        song.append(f"{i} bottle{'s' if i > 1 else ''} of beer on the wall, "
                    f"{i} bottle{'s' if i > 1 else ''} of beer.")
        song.append((f"Take one down and pass it around, "
                     f"{i - 1} bottle{'s' if i - 1 > 1 else ''} "
                     f"of beer on the wall.")
                    if i > 1 else
                    (f"Take it down and pass it around, "
                     f"no more bottles of beer on the wall."))
        if i > start - take + 1:
            song.append("")

    return song
