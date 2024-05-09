import random
import re

class DiceRoll:
    """Class representing a basic dice roll."""

    def __init__(self, num_dice, num_sides):
        """Initialize the dice roll with the number of dice and number of sides per die.

        Args:
            num_dice (int): Number of dice to roll.
            num_sides (int): Number of sides per die.
        """
        self.num_dice = num_dice
        self.num_sides = num_sides

    def roll(self):
        """Simulate rolling the dice and return the result as a list of individual rolls.

        Returns:
            list: List of individual dice rolls.
        """
        return [random.randint(1, self.num_sides) for _ in range(self.num_dice)]

class DiceRollWithModifier(DiceRoll):
    """Class representing a dice roll with a modifier."""

    def __init__(self, num_dice, num_sides, modifier):
        """Initialize the dice roll with the number of dice, number of sides per die, and modifier.

        Args:
            num_dice (int): Number of dice to roll.
            num_sides (int): Number of sides per die.
            modifier (int): Modifier to add to the total points.
        """
        super().__init__(num_dice, num_sides)
        self.modifier = modifier

    def roll(self):
        """Simulate rolling the dice with modifier and return the total points, individual rolls, and modifier.

        Returns:
            tuple: Total points, list of individual dice rolls, and modifier.
        """
        rolls = super().roll()
        total_points = sum(rolls)
        total_points += self.modifier
        return total_points, rolls, self.modifier

# Usage
input_str = "2d20+1"
match = re.match(r"([1-9][0-9]*)(d)([1-9][0-9]*)(([-+])([0-9]+))?", input_str)
if match:
    num_dice = int(match.group(1))
    num_sides = int(match.group(3))
    modifier = int(match.group(6)) if match.group(6) else 0

    if modifier:
        roller = DiceRollWithModifier(num_dice, num_sides, modifier)
        total_points, rolls, modifier = roller.roll()
    else:
        roller = DiceRoll(num_dice, num_sides)
        rolls = roller.roll()
        total_points = sum(rolls)
    print(total_points, rolls, modifier)
else:
    print("Invalid input format")
