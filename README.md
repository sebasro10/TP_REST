# TP REST

**Author**: Sebastian Romero <sebastian.romero@imt-atlantique.net>

This repository has a folder for each microservice:

* `/booking`
* `/movie`
* `/showtime`
* `/user`

In the `docker-compose.yml` file you can see the information about the services and their ports to perform the http request.

## What was made of the TP?

In this repository from commits you can clearly see the progress of the TP:

* Commit [Tutorial Flask](https://github.com/sebasro10/TP_REST/commit/2f7655c4320306356f44db0d216da8565e92354e)
* Commit [Tutorial OpenAPI](https://github.com/sebasro10/TP_REST/commit/955555da9f37c024800f9056ff2a867a09048da9)
* Commit [docker-compose.yml](https://github.com/sebasro10/TP_REST/commit/02f7e98dab233344ee646def90355a42693bf5b7) : Container names are added to perform the request using these
* Commit [TP vert -> 1 et 2](https://github.com/sebasro10/TP_REST/commit/eb14aa7a2b682efd6fa8d734dfcc43f2b207df51)
* Commit [TP vert -> 3](https://github.com/sebasro10/TP_REST/commit/dead0bd5611ae512bfeca588a0f720a69fc8737b)
* Commit [TP vert -> 4](https://github.com/sebasro10/TP_REST/commit/35c6458f88fd20933919888bbe4b0221346239c1)
* Commit [TP vert -> 5 et 6](https://github.com/sebasro10/TP_REST/commit/f7ea9198d8336ce7d48fe83419633fb2a8e4fc11)
* Commit [TP bleu](https://github.com/sebasro10/TP_REST/commit/890a08d1fd2b0b3fd606af9238f764cb9762de02) : According to what I understood from this exercise, I modified the PUT method to facilitate the API discovery.
* Commit [TP rouge](https://github.com/sebasro10/TP_REST/commit/8e1c6a9af6a85a2f812e6b41cf7e5028c976930a)

## Run project

Build or rebuild services
```bash
docker-compose build
```

Create and start containers
```bash
docker-compose up
```

Stop and remove containers, networks
```bash
docker-compose down
```

## Tests from Postman

You can test each service from Postman by following the steps below:

* In Postman click on "Import" -> "Upload Files"
* Select the file with the contract (Each service folder has a file with `.yaml` extension containing the OpenAPI contract)
* Select the option "Generate collection from imported APIs" and in "Link this collection as" select "Test suite"
* Click on "Import"

Now, a collection has been created and you can test the methods.
