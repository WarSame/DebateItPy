import { Injectable } from '@angular/core';
import { SERVER_URL } from 'src/app/app.component';
import { HttpClient } from '@angular/common/http';
import { User } from 'src/app/components/user/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private USER_URL = SERVER_URL + '/api/u';

  constructor(private http: HttpClient) { }

  getUser(id: string) {
    return this.http.get<User>(this.USER_URL, {});
  }

  createUser(user: User) {
    return this.http.post(this.USER_URL, user);
  }
}
