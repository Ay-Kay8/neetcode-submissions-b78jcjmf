public class Solution {

    public string Encode(IList<string> strs) {
		string encoded = "";
		foreach (string str in strs) {
			encoded += str.Length + "#" + str;
		}
		return encoded;
    }

    public List<string> Decode(string s) {
		int i = 0;
		List<string> decoded = new List<string>();
		while (i < s.Length) {
			string num = "";
			while (char.IsDigit(s[i])) {
				num += s[i];
				i++;
			}
			
			// We then encounter a #
			i++;
			
			string word = "";
			int limit = i + int.Parse(num);
			while (i < limit) {
				word += s[i];
				i++;
			}
			decoded.Add(word);
		}
		
		return decoded;
   }
}