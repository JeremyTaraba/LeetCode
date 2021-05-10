public class Solution {
    public int NumUniqueEmails(string[] emails) {
        
        if (emails == null || emails.Length == 0)
            return 0;

        var uniqueID = new HashSet<string>(); 
        foreach(var email in emails){
            var splitNames = email.Split('@');
            var localName = splitNames[0];
            var domainName = splitNames[1];
            localName = localName.Replace(".", "");
            var userName = localName.Split('+')[0];
            uniqueID.Add(userName + "@" + domainName); 
        }

        return uniqueID.Count; 
    
    }
}

/*
Notes:
At first I was going to parse the emails into a sorted list and just check how many unique emails were in that list
But this is the perfect case to use a hashset. A hashset will keep each entry unique because it hashes the 
data before it is entered into the list. Those with the same name will be hashed the same way and put into the same bucket

Constraints:
1 <= emails.length <= 100
1 <= emails[i].length <= 100
email[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.

*/