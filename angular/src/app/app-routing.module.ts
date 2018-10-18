import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RouterModule, Routes } from '@angular/router';

import { TopGeneralFeedComponent } from './components/top-general-feed/top-general-feed.component';
import { GetPostComponent } from './components/post/get-post/get-post.component';
import { CreatePostComponent } from './components/post/create-post/create-post.component';
import { CreateCommunityComponent } from './components/community/create-community/create-community.component';
import { GetCommunityComponent } from './components/community/get-community/get-community.component';



const appRoutes: Routes = [
  { path: 'p', component: CreatePostComponent},
  { path: 'p/:id', component: GetPostComponent},
  { path: 'c', component: CreateCommunityComponent},
  { path: 'c/:id', component: GetCommunityComponent},
  { path: '', component: TopGeneralFeedComponent}
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(
      appRoutes,
      {enableTracing: false}
    )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
