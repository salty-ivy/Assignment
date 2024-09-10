# Questions for Django Trainee at Accuknox  [Original Doc](https://docs.google.com/document/d/1LdyiwxVLw6X8LIaLibtCHMIvQfYLHfMVIcB7gVb8Bkw/edit?usp=sharing)

## Q1.

Signals are like hooks that act between senders and receivers. The sender function calls a `send()` function at a particular event and calls the receiver function that is dispatched and hooked to it. For example, signals like `post_save`, `pre_save`, `request_finished`, `template_rendered`, `pre_migrate`, etc.

Signals have two methods for sending a call to the receiver: `send` (synchronous) and `asend` (asynchronous).

**Answer:** All signals, except those in asynchronous contexts, by default call the `send` method, making them synchronous.

**Async Context:** Signals are asynchronous in cases like an async request/response lifecycle in an async server or with new model methods like `asave`.

If we check the console, we can see the logs in the expected order. This demonstrates that the code runs synchronously in sequence.

<img width="605" alt="image" src="https://github.com/user-attachments/assets/3af186f9-5881-4beb-99d8-63187bf3b6fa">
<img width="612" alt="image" src="https://github.com/user-attachments/assets/fb2a2b22-dfcc-4f74-bf92-5afdc0acd924">


---

## Q2.

In support of the answer for Question 1, it is evident that signals run synchronously by default and within the same thread. For senders to pass context data to receivers, both need to operate in the same thread.

We can prove this by printing the thread ID from the caller and handler and checking if they match using the `threading` module.

When saving a `Pizza` class in the Python Django shell, we observe that the threading ID matches.

**Answer:** Yes, signals run in the same thread by default.

<img width="611" alt="image" src="https://github.com/user-attachments/assets/a9e84c44-ee6f-4321-b278-6e4dab2766c9">

<img width="634" alt="image" src="https://github.com/user-attachments/assets/ea51bcfb-2c4c-4b01-b812-992d9d4903de">

Now when saving a pizza class in python django shell we can see if the threading ID matches or not.

<img width="615" alt="image" src="https://github.com/user-attachments/assets/250c080a-7f0f-4994-89c4-0f1894befd87">

Yes they do so,

Ans: yes, they run in same thread by default

**Though signals can be sent from different context when running in async enviroment** 

**checkout my work over making `StaticFilesPanel` async/ASGI compatible using `Signals`  and `ContextVars` ( local thread storage mechanis for async )**

https://github.com/jazzband/django-debug-toolbar/pull/1983
 
---

## Q3.

Signals like `post_save`, `pre_save`, `post_delete`, and `pre_delete` are called within the same database transactions. This ensures that handlers, which might perform actions like logging or creating associated model objects, are executed before the original commit.

For example, when using `transaction.atomic()`, we ensure that everything runs within a single transaction, meaning the `pre_save` handler must also run within that transaction if signals are running in the same context.

**Answer:** Since `pre_save` runs with the `save` method within `transaction.atomic()`, this means signals run within the same DB transaction.

<img width="540" alt="image" src="https://github.com/user-attachments/assets/30f55aa2-38a7-42d9-9562-d5cf6c320a86">


---

## About Me

I am **Aman Pandey**, a final-year student and an open-source developer, working with Python/Django-based open-source organizations. I have 3-4 years of experience building Django-based projects and applications.

I am a technical member and a **[Google Summer of Code 2023](https://summerofcode.withgoogle.com/archive/2023/projects/Zs8nVswq)** contributor to **[WagtailCMS](https://wagtail.org/)**, a Django-based content management system. I also contribute to the **Django Software Foundation**, helping developers build and enhance frameworks and packages like **django-debug-toolbar**.

Currently, I am a **[Google Summer of Code 2024 Contributor](https://summerofcode.withgoogle.com/programs/2024/projects/iXVvyGYp)** at the **Django Software Foundation**, working on adding async compatibility with **[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)**. Additionally, I work as a **Backend Engineer** at **Cityflo**.

- **GitHub**: [https://github.com/salty-ivy](https://github.com/salty-ivy)
- **LinkedIn**: [https://www.linkedin.com/in/aman-pandey-06a600217/](https://www.linkedin.com/in/aman-pandey-06a600217/)
- **Resume**: [Aman Pandey Resume](https://drive.google.com/drive/folders/1f-FIHjig2_Th5Rqr5QC1O6-L9up2Vnfc?usp=sharing)

---

## CTC Details

- **Current CTC**: 12 LPA
- **Expected CTC**: 15-16 LPA
- **Notice Period**: Can join within 40 days
