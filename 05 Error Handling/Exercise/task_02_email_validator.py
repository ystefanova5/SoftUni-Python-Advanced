class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()

    if email == "End":
        break

    name = email.split("@")[0]
    domain = email.split(".")[-1]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.count("@") != 1:
        raise MustContainAtSymbolError("Email must contain @")

    if domain not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
