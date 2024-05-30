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
        total_points = sum(rolls) + self.modifier
        return total_points, rolls, self.modifier

def skill_opposed(input_str):
    match = re.search(r"(\d+)$", input_str.strip())
    return int(match.group(1)) if match else 0

def match_main(input_str):
    return_data = {}
    match_str = r"(\d+)d(\d+)([+-]\d+)?"
    match = re.match(match_str, input_str)
    
    if match:
        num_dice = int(match.group(1))
        num_sides = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0
        max_point = num_dice * num_sides + modifier

        if modifier:
            roller = DiceRollWithModifier(num_dice, num_sides, modifier)
            total_points, rolls, modifier = roller.roll()
            return_data["modifier"] = modifier
        else:
            roller = DiceRoll(num_dice, num_sides)
            rolls = roller.roll()
            total_points = sum(rolls)

        return_data["total_points"] = total_points
        return_data["rolls"] = rolls

    skill_opposed_int = skill_opposed(input_str)
    if skill_opposed_int:
        if "coc" in input_str.lower():
            if total_points <= skill_opposed_int:
                if total_points == 1:
                    return_data["result"] = "大成功"
                elif total_points <= skill_opposed_int / 5:
                    return_data["result"] = "成功 extreme"
                elif total_points <= skill_opposed_int / 2:
                    return_data["result"] = "成功 hard"
                else:
                    return_data["result"] = "成功 regular"
            elif total_points > skill_opposed_int:
                if total_points == max_point:
                    return_data["result"] = "大失敗"
                else:
                    return_data["result"] = "失敗"
        elif "dnd" in input_str.lower():
            if total_points >= skill_opposed_int:
                return_data["result"] = "成功"
            else:
                return_data["result"] = "失敗"
    
    return return_data

# Example usage:
input_str = "2d20+5 coc 30"
result = match_main(input_str)
print(result)
