verbose = 1

class Score:

    @staticmethod
    def scoregame(contractlevel, contractsuit, numtricks):
        score = 0
        # Game Contract Check
        gamecon = (contractlevel * 10) + contractsuit

        if contractlevel + 6 - numtricks > 0:
            score = -50 * (contractlevel + 6 - numtricks)
            if verbose:
                print("Loss")
            return score

        else:
            if contractsuit == 0 or contractsuit == 1:
                score = 20 * (numtricks - 5)
                if verbose:
                    print("Minor")
            elif contractsuit == 2 or contractsuit == 3:
                score = 30 * (numtricks - 5)
                if verbose:
                    print("Major")
            else:
                score = 40 + 40 * (numtricks - 7)
                if verbose:
                    print("No Trump")

            if gamecon >= 34 and gamecon <= 54:
                score += 300
                if verbose:
                    print("Game Contract")
            elif contractlevel == 6:
                score += 500
                if verbose:
                    print("Small Slam")
            elif contractlevel == 7:
                score += 1000
                if verbose:
                    print("Grand Slam")
            else:
                score += 50
                if verbose:
                    print("Part Score")

            return score
