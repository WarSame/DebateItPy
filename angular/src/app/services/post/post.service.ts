import { Injectable } from '@angular/core';
import { SERVER_URL } from 'src/app/app.component';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PostService {
  private POST_URL = SERVER_URL + '/p';

  constructor(private http: HttpClient) {}

  getPost(id: string) {
    return this.http.get<void>(this.POST_URL + '/' + id, {});
  }
}
