public class Solution {


    public string Encode(IList<string> strs) {
		StringBuilder sb = new StringBuilder();
		
		foreach (string str in strs) {
			sb.Append(str.Length);
			sb.Append("#");
			sb.Append(str);
		}
		
		return sb.ToString();
    }

    public List<string> Decode(string s) {
		int i = 0;
		List<string> decoded = new List<string>();

		while (i < s.Length) {
			int num = 0;
			while (s[i] != '#') {
				num = num * 10 + s[i] - '0';
				i++;
			}

			// We then encounter a #
			i++;
			
			// Start at i, and take "num" characters
			decoded.Add(s.Substring(i, num));
			i += num;
		}
		
		return decoded;
   }
}