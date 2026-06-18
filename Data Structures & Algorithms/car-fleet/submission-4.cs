public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        var posAndSpeed = new ValueTuple<int, int>[position.Length];
		
		for (int i = 0; i < position.Length; i++) {
			posAndSpeed[i] = (position[i], speed[i]);
		}
		
		Array.Sort(posAndSpeed, (a, b) => b.CompareTo(a));
		
		// no need for a stack, just keep track of previous speed
		double prevTime = 0;
		int carFleets = 0;
		foreach (var (p, s) in posAndSpeed) {
		
			// make sure this uses doubles and not integer division
			// since you can get to target in 4.5 hours
			double time = (double)(target - p) / s;
			
			if (time > prevTime) {
				carFleets++;
				// Only override the time when there's another car fleet
				// We want to always keep track of the slowest time
				prevTime = time;
			}
		}

		return carFleets;
    }
}
