

bug tracker application, built with Django that:

*   requires logging in, but people who aren't logged in _cannot_ create accounts (don't want any random person to see bugs in your application!)
*   use a custom user model to replace the built-in one
*   has a homepage that shows all tickets, arranged in separate sections according to current ticket status (i.e. New, In Progress, Done, Invalid)
*   allows filing/creating tickets
*   has a ticket detail page
*   allows assigning a ticket to the currently logged in user
*   allows marking a ticket as invalid
*   allows marking a ticket as complete
*   allows editing tickets (we will limit this to Title and Description, do not include other any of the other fields)
*   has a user detail page where you can see:
    *   the current tickets assigned to a user
    *   which tickets that user has filed
    *   which tickets that user completed

When a ticket is filed/created, it should have the following settings:

*   Status: New
*   User Assigned: None
*   User who Completed: None
*   User who filed: Person who's logged in

When a ticket is assigned, these change as follows:

*   Status: In Progress
*   User Assigned: person the ticket now belongs to
*   User who Completed: None

When a ticket is Done, these change as follows:

*   Status: Done
*   User Assigned: None
*   User who Completed: person who the ticket used to belong to

When a ticket is marked as Invalid, these change as follows:

*   Status: Invalid
*   User Assigned: None
*   User who Completed: None
