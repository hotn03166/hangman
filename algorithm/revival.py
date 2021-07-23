# 再起

def bottles_of_beer(bob):
    """
    Prints Bottle of Beer on the Wall lyrics
    
    :param bob: Must be a positive integer.
    
    """

    # 再起終了条件の用意
    if bob < 1:
        print(\
            """
            No more bottles of beer one the wall.
            No more bottles of beer.
            """
            )
        return

    tmp = bob

    # 再起終了条件に進んでいく
    bob -= 1

    print(\
        """
        {} bottles of beer one the wall.
        {} bottles of beer.

        Take one down, pass it around,
        {} bottles of beer one the wall.
        
        """.format(tmp, tmp, bob)
        )

    # 関数自身を呼び出す
    bottles_of_beer(bob)

bottles_of_beer(99)
    
