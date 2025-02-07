# Nestjs basic configuration

this guidance is tested and best to use in Node 22.13.1

## Initial install

1. Install nest cli if not exist

```
npm i -g @nestjs/cli
```

2. Initialize nest project

```
nest new project-name
```

## Required package with MiroORM

```
npm install --save @nestjs/passport passport passport-local @nestjs/jwt passport-jwt dotenv class-validator class-transformer cookie-parser @nestjs/config @nestjs/axios axios @nestjs/terminus bcrypt @mikro-orm/core @mikro-orm/nestjs @mikro-orm/mariadb @mikro-orm/migrations @mikro-orm/seeder uuid
npm install --save-dev @types/passport-jwt @types/passport-local @types/cookie-parser @types/bcrypt @mikro-orm/cli @types/uuid
```
