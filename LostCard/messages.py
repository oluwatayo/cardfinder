# automated mail messages!!!
def message_perfect_owner():
    message = "Hey!! Your missing card has been found. Please kindly" \
              " contact the finder using the email or phone number below. "
    return message

def message_perfect_finder():
    message = "Hey!! You found a card. We already sent a mail to the owner to contact you. " \
              "But if you don't get any message, " \
              "please kindly contact the owner via the email address or phone number below"
    return message

def message_not_perfect_owner():
    message = "Hey!! It seems like someone found your missing card. " \
              "Please contact the person using the email or phone Number below"
    return message

def message_not_perfect_finder():
    message = "Hey!! Seems like you found someones card." \
              "We alredy sent a mail to the owner of the card to contact you. " \
              "If you don't receive any mail or call from the owner," \
              " please kindly contact the owner of the card via the mail or phone number below"
    return message

def no_match_found():
    message = "Hey!! Thanks for submitting details about the card you found on this platform. " \
              "Unfortunately, the card you found has not been reported missing yet. But don't worry, " \
              "we'll keep checking for matches each time a card is reported missing and inform you if we find a match. " \
              "Please Do well to keep the card safe with you. "
    return message

def message_perfect_lost_owner():
    message = "Hey!! Your missing card has been found Please contact the finder via the mail or phone number below "
    return message

def message_perfect_lost_finder():
    message = "Hey!! The card you found has been reported missing. Please contact the owner of the card via the mail" \
              "or phone number below"
    return message

def message_not_perfect_lost_owner():
    message  = "Hey!! It seems like someone found your missing card, Please contact the finder " \
               "via the mail address or phone number below"
    return message
def message_not_perfect_lost_finder():
    message = "Hey!! It seems like the card you found has been reported missing ." \
              "Please contact the owner of the card via the email or phone number below "
    return message

def no_match_lost():
    message = "Hey!! Your Missing card has not been found yet. Anyways don't worry we'll keep checking for matches " \
              "and we'll  let you know when your card is found"
    return message