import { Injectable } from '@angular/core';
import { SERVER_URL } from 'src/app/app.component';
import { HttpClient } from '@angular/common/http';
import { Post } from 'src/app/components/post/post';

@Injectable({
  providedIn: 'root'
})
export class PostService {
  private POST_URL = SERVER_URL + '/api/p/';

  constructor(private http: HttpClient) {}

  getPost(id: string) {
    return this.http.get<Post>(this.POST_URL + id, {});
  }

  createPost(post: Post) {
    return this.http.post(this.POST_URL, post);
  }
}
