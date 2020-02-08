Model Architecture planning

Membership
    -slug
    -type(free, pro, enterprise)
    -price
    -stripe plan id

UserMembership
    -user                   (foreign key to user)
    -stripe customer id
    -membership type        (foreign key to membership)

Subscription
    -user membership        (foreign key to usermembership)
    -stripe subsription id
    -active

Course
    -slug
    -title
    -description
    -allowed memberships      (ManyToManyField key to membership)

Lesson
    -slug
    -title
    -Course         (foreign key to Course)
    -position
    -video
    -thumbnail
