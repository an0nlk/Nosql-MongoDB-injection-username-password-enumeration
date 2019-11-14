# Nosql injection username and password enumeration script
Using this script, we can enumerate Usernames and passwords of Nosql(mongodb) injecion vulnerable web applications.
<br /><br />
Exploit Title: Nosql injection username/password enumeration.<br />
Auther: Kalana Sankalpa (Anon LK).<br />
Website: https://blogofkalana.wordpress.com/2019/11/14/nosql-injection-username-and-password-enumeration/<br />

## How to run 

### Usage

```
nosqli-user-pass-enum.py [-h] [-u URL] [-up parameter] [-pp parameter] [-op parameters] [-ep parameter] [-sc character] [-m Method]
```

### Example

```
python nosqli-user-pass-enum.py -u http://example.com/index.php -up username -pp password -ep username -op login:login,submit:submit
```

### Arguments

| Arguments        | Description           |
| ------------- |:-------------:|
| -h, --h      | show this help message and exit |
| -u URL      | Form submission url. Eg: http://example.com/index.php      |
| -up parameter | Parameter name of the username. Eg: username, user      |
| -pp parameter | Parameter name of the password. Eg: password, pass      |
| -op parameters | Other paramters with the values. Separate each parameter with a comma(,). <br />Eg: login:Login, submit:Submit      |
| -ep parameter | Parameter that need to enumarate. Eg: username, password      |
| -sc character | Character or letter that need to start from. Eg: a.b,c      |
| -m Method | Method of the form. Eg: GET/POST      |
