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