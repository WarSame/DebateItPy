import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RouterModule, Routes } from '@angular/router';

import { TopGeneralFeedComponent } from './components/top-general-feed/top-general-feed.component';
import { GetPostComponent } from './components/post/get-post/get-post.component';



const appRoutes: Routes = [
  { path: 'p/:id', component: GetPostComponent},
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
