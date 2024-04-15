from faker import Faker


class Generate:

    last_generated_password = None
    last_generated_email = None
    last_generated_name = None

    @classmethod
    def full_creds(cls):
        return {
            'email': cls.email(),
            'password': cls.password(),
            'name': cls.name()
        }

    @classmethod
    def name(cls):
        cls.last_generated_name = Faker().name()
        return cls.last_generated_name

    @classmethod
    def email(cls):
        cls.last_generated_email = Faker().email()
        return cls.last_generated_email

    @classmethod
    def password(cls):
        cls.last_generated_password = Faker().password()
        return cls.last_generated_password
