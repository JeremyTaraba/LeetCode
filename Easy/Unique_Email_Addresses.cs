/*
Prompt:
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.


*/



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